var contactManager = angular.module('counseling', []);

contactManager.controller('mainCtrl',
    function ($scope) {
        $scope.showSection = function (section) {
            $scope.template = section;
        };
        $scope.showMain = function () {
            $scope.showSection("about");
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