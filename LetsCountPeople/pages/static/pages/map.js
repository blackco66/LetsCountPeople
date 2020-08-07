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
    '<div>',
    ' <h3>' + locName + '</h3>',
    ' <p>' + locAddress + ' | ' + locType + '<br/>',
    ' 현재 사람 수: ' + locPopulation,
    ' </p>',
    '</div>',
  ].join('');

  const infowindow = new naver.maps.InfoWindow({
    content: contentString,
    maxWidth: 140,
    backgroundColor: '#eee',
    borderColor: '#2db400',
    borderWidth: 5,
    anchorSize: new naver.maps.Size(30, 30),
    anchorSkew: true,
    anchorColor: '#eee',
    pixelOffset: new naver.maps.Point(20, -20),
  });

  naver.maps.Event.addListener(marker, 'click', function (e) {
    if (infowindow.getMap()) {
      infowindow.close();
    } else {
      infowindow.open(map, marker);
    }
  });
}

drawMap();

$('[data-onload]').each(function () {
  eval($(this).data('onload'));
});
