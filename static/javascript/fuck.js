var contactManager = angular.module('counseling', []);

contactManager.controller('mainCtrl',
    function ($scope, $http) {
        $scope.showSection = function (section) {
            $http.get('/api/v1/' + section).
                success(function (data, status, headers, config) {
                    $scope.content = data.content;
                    $scope.header = data.header;
                    // this callback will be called asynchronously
                    // when the response is available
                }).
                error(function (data, status, headers, config) {
                    // called asynchronously if an error occurs
                    // or server returns response with an error status.
                });
        };
        $scope.showMain = function () {
            $scope.showSection("main");
        };

        $scope.showResume = function () {
            $scope.showSection("resume");
        };
        $scope.showContact = function () {
            $scope.showSection("contact");
        };
        $scope.showTestimonials = function () {
            $scope.showSection("testimonials");
        };

        $scope.showMain();

    });