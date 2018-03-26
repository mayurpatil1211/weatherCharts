angular.module('routerApp')
    .controller('readingController', ['$scope', '$http', '$timeout', '$location', function($scope, $http, $timeout, $location) {
        
        $scope.save_data = true
        $scope.loadme = false

        //Get year list for select tag
        function get_years() {
            $http.get('http://18.217.244.65:8080/api/get_years')
                .then(function(res, err) {
                    if (res) {
                        $scope.years = res.data.years
                    } else {
                        $scope.years = [2018]
                    }

                })
        }
        get_years();


        //Filter data or get data on app init
        $scope.startFilter = function(filter) {

            console.log($scope.filter)
            if ($scope.filter) {
                //get filter attributes from view
                var year_attribute = $scope.filter.year;
                var country_attribute = $scope.filter.country;
            } else {
                //assign filter attribute if not present

                var year_attribute = new Date().getFullYear();
                var country_attribute = 'UK';
            }

            $scope.loading = true;
            //call api
            $http.get('http://18.217.244.65:8080/api/get_data/' + country_attribute + '/' + year_attribute)

                .then(function success(response) {

                    $scope.message = response.data.result;

                    $scope.country = $scope.message.country
                    $scope.year = $scope.message.year

                    $scope.maxTemplabels = $scope.message.maxTemp.labels;
                    $scope.maxTempdata = $scope.message.maxTemp.value;

                    $scope.minTemplabels = $scope.message.minTemp.labels;
                    $scope.minTempdata = $scope.message.minTemp.value;

                    $scope.meanTemplabels = $scope.message.meanTemp.labels;
                    $scope.meanTempdata = $scope.message.meanTemp.value;

                    $scope.rainFalllabels = $scope.message.rainfall.labels;
                    $scope.rainFalldata = $scope.message.rainfall.value;

                    $scope.sunshinelabels = $scope.message.sunshine.labels;
                    $scope.sunshinedata = $scope.message.sunshine.value;
                    $scope.loading = false;
                    $scope.loadme = true
                }, function error(response) {
                    $scope.loading = false;
                    console.log(response)
                });
        }
        //call function on app init
        $scope.startFilter();


        $scope.save_new_data = function() {
            $scope.loading = true;
            $scope.save_data = false
            $http.post('http://18.217.244.65:8080/api/save_data').then(function(res, err) {
                if (res) {
                    $scope.save_data = true
                    console.log(res)
                    $scope.errorMsg = false
                    $scope.successMsg = res.data.message;
                    $scope.loadme = true
                    $scope.loading = false;

                    $timeout(function() {
                        $scope.successMsg = false
                        $location.path('/readings');
                    }, 2000);

                } else {
                    $scope.loading = false;
                    $scope.save_data = true
                    console.log('Failed to Save New Data')
                    $scope.successMsg = false
                    $scope.errorMsg = err.data.message;
                    $scope.loadme = true
                    $timeout(function() {
                        $scope.errorMsg = false
                        $location.path('/readings');
                    }, 2000);
                }
            });
        }

        //chart function to get co-ordinates when click event occure
        $scope.onClick = function(points, evt) {
            console.log(points, evt);
        };


    }])