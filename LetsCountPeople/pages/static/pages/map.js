function changeGym(name, address, lat, lon, pop) {
  document.getElementById('gymname').value = name;
  document.getElementById('gymaddress').value = address;
  if (lat != 'None') {
    document.getElementById('gymlatitude').value = lat;
    document.getElementById('gymlongitude').value = lon;
  } else {
    // lat, lon 구해서 db에 저장하도록 하자.
  }
  if (pop != 'None') {
    document.getElementById('gympopulation').value = pop;
  } else {
    // 재경아 화이팅!
  }
  drawMap();
}
function drawMap() {
  const locName = document.getElementById('gymname').value;
  const locAddress = document.getElementById('gymaddress').value;
  const latitude = Number(document.getElementById('gymlatitude').value);
  const longitude = Number(document.getElementById('gymlongitude').value);
  const locType = '헬스장';
  const locPopulation = Number(document.getElementById('gympopulation').value);

  const locPosition = new naver.maps.LatLng(latitude, longitude);
  const map = new naver.maps.Map('map', {
    center: locPosition,
    zoom: 15,
  });
  const marker = new naver.maps.Marker({
    map: map,
    position: locPosition,
  });

  const contentString = [
    '<div style="font-family:serif; padding:5px;">',
    '<div style="font-size:16px;">' + locName + '</div>',
    '<div style="font-size:12px;">' + locAddress + '</div>',
    '<div style="font-size:14px;">' +
      ' 현재 사람 수: ' +
      locPopulation +
      '</div>',
    '</div>',
  ].join('');

  const infowindow = new naver.maps.InfoWindow({
    content: contentString,
    maxWidth: 250,
    backgroundColor: '#F0F8FF',
    borderColor: '#1c7ed6',
    borderWidth: 1,
    anchorSize: new naver.maps.Size(10, 10),
    anchorSkew: true,
    anchorColor: '#F0F8FF',
    pixelOffset: new naver.maps.Point(0, -5),
  });

  naver.maps.Event.addListener(marker, 'click', function (e) {
    if (infowindow.getMap()) {
      infowindow.close();
    } else {
      infowindow.open(map, marker);
    }
  });
  infowindow.open(map, marker);
}

drawMap();
