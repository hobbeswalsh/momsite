app = angular.module('counseling', [])

mainPage = {
  header: "About Annie",
  content: [
    "Deep v Shoreditch ex authentic. Leggings taxidermy Truffaut, do ut chambray salvia velit High Life
    paleo aesthetic tofu Etsy cray flannel. Beard DIY reprehenderit, elit sriracha 3 wolf moon dreamcatcher
    consectetur bicycle rights tattooed velit yr small batch gastropub kale chips. Nesciunt Bushwick occupy
    Thundercats, assumenda chillwave enim 8-bit consequat gentrify chia. Accusamus Kickstarter fingerstache
    lumbersexual freegan ea. Aliqua freegan beard magna, Truffaut Neutra semiotics YOLO fingerstache small
    batch messenger bag chambray. Meh irure dolor elit.",

    "8-bit drinking vinegar reprehenderit, qui organic tote bag anim yr VHS Pitchfork.
    Vice forage Pinterest, Williamsburg magna pickled Truffaut Etsy. Adipisicing raw denim vinyl,
    eu aesthetic butcher sriracha. Sunt mustache PBR swag Thundercats seitan authentic accusamus.
    Lo-fi occaecat crucifix sriracha. YOLO seitan pariatur, Thundercats lomo umami proident tofu occaecat
    ad paleo. Cold-pressed est slow-carb, commodo organic craft beer chia deep v vegan hoodie PBR&B dolor."

  ]
}

resumePage = {
  header: "Qualifications",
  content: [
    "This would be a long résumé page",
  ]
}

app.controller('mainCtrl', ($scope) ->
  this.showMain = ->
    $scope.header = "FUCK"
    $scope.content = "YOU"
  this.showResume = ->
    console.log("god damnit")
    $scope.header = "GOD FUCKING DAMNIT"
    $scope.content =  "FUCCCCKCKKK"
  this.showResume()
  this.showMain()
)