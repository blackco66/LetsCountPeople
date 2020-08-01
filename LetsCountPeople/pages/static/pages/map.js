function drawMap() {
  const locName = document.getElementById("gymname").value;
  const locAddress = "서울 관악구 관악로 195 관악위버폴리스 B동 2층";
  const latitude = 37.482792;
  const longitude = 126.95328;
  const locType = "헬스장";
  const locPopulation = 34;

  const locPosition = new naver.maps.LatLng(latitude, longitude);
  const map = new naver.maps.Map("map", {
    center: locPosition,
    zoom: 15,
  });
  const marker = new naver.maps.Marker({
    map: map,
    position: locPosition,
  });

  const contentString = [
    "<div>",
    " <h3>" + locName + "</h3>",
    " <p>" + locAddress + " | " + locType + "<br/>",
    " 현재 사람 수: " + locPopulation,
    " </p>",
    "</div>",
  ].join("");

  const infowindow = new naver.maps.InfoWindow({
    content: contentString,
    maxWidth: 140,
    backgroundColor: "#eee",
    borderColor: "#2db400",
    borderWidth: 5,
    anchorSize: new naver.maps.Size(30, 30),
    anchorSkew: true,
    anchorColor: "#eee",
    pixelOffset: new naver.maps.Point(20, -20),
  });

  naver.maps.Event.addListener(marker, "click", function (e) {
    if (infowindow.getMap()) {
      infowindow.close();
    } else {
      infowindow.open(map, marker);
    }
  });
}

drawMap();

