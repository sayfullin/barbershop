var str,n, map;
markerPom = [];
$(document).ready(function() {
    barbershops = [];
    $.ajax({
      url: "api/barbershops/all_data/",
      success : function(data) {
        barbershops = data;
        for(var i =0; i< barbershops.length; i++){
            var item_div = $('<div class="item">');
            item_div.attr('attr-id', barbershops[i].id);
            var item_link = $('<div class="img-cnt">');
            var pp = barbershops[i].photos[0];
            item_link.css({'background': 'url('+pp+")no-repeat center"});
            item_div.append(item_link);
            var item_info_div = $('<div class="item-info">');
            var item_raiting = $('<div class="raiting">');
            item_raiting.text(barbershops[i].stars);
            var item_name = $('<h3>');
            item_name.text(barbershops[i].name);
            var item_p = $('<p>');
            item_p.text(barbershops[i].address);
            item_info_div.append(item_raiting);
            item_info_div.append(item_name);
            item_info_div.append(item_p);

            item_div.append(item_info_div);
            $('#container2').append(item_div);
            item_div.click(itemClick)


            var myLatlng = new google.maps.LatLng(barbershops[i].latitude , barbershops[i].longitude) ;
            var mapOptions = {
                zoom: 11,
                center: myLatlng
            }
            var markerS = new google.maps.Marker({
                    position: myLatlng,
                    map: map,
                    index: i,
                    icon: 'static/images/smallmarker.png'
            });
            markerS.set("index", i);
            var markerB = new google.maps.Marker({
                    position: myLatlng,
                    index: i,
                    icon: 'static/images/bigmarker.png'
            });
            markerPom.push([markerS, markerB]);
            google.maps.event.addListener(markerS, 'click', function() {
                selectItem(this.index);
            });
        }
        allSmallMarket();
      }
    });

    function allSmallMarket(){
        markerPom.forEach(function(entry) {
            entry[0].setMap(map);
            entry[1].setMap(null);
        });
    }

    $('#b-info-cont .item').click(function() {
        var bbName = $(this).find('h3');
        var bbAddress = $(this).find('p');
        $('#barber-info-container h4').innerHtml(bbName);
        $('#barber-info-container pre').innerHtml(bbAddress);
    });

    var mnW = $('#b-info-cont').width();

    $('#footer').width(mnW);


    str = '{"name":"Chop-Chop","id":"1","parametes":[{"lat": 55.762091},{"lng": 49.1657973}]}';
    n = JSON.parse(str);
    initMap();

    var plc = '{"name":"Chop-Chop","time":"9:00-16:00","phone":"8(999)999-99-99","web-site":"www.example.ru","photos":[{"url":"aaaaa","alt":"aaaa"},{"url":"aaaaa","alt":"aaaa"}],"workers":[{"id":"1","name":"Иванов Иван Иванович","photo":"aaa"},{"id":"2","name":"Иванов Иван Иванович","photo":"aaa"}]}';
    var barber = JSON.parse(plc);

    // $('#b-info-cont h2').text(barber.name);



    $('#date-slider .date-slide').click(function() {
        $('#date-slider .date-slide').removeClass('active');
        $(this).addClass('active');
    });

    $('.time-item').click(function() {
        $('.time-item').removeClass('active');
        $(this).addClass('active');
    });

    $('#sign-up form div').click(function() {
        $('#sign-up form div').removeClass('active');
        $(this).addClass('active');
    });

    itemClick = function(event) {
        var itemIndex = $(event.target).parent('.item').attr('attr-id') - 1;
        selectItem(itemIndex)
    };

    selectItem = function(itemIndex){
        var vv = $(this).find('.item-info').find('h3').text();
        $('#booking-container form input[name="bbShop"]').val(barbershops[itemIndex].id);
        $('#barber-photo-slider').html('<img src=' + barbershops[itemIndex].photos[0].url + '>')
        $('#booking-container #booking-info .bb-name').html(barbershops[itemIndex].name);
        $('#barber-info-container h4').text(barbershops[itemIndex].name);
        $('#barber-info-container pre').text(barbershops[itemIndex].address);
        $('#barber-info-container p.barber-type').text(barbershops[itemIndex].saloon_type);
        $('#barber-info-container p.about').text(barbershops[itemIndex].description);
        $('#barber-info-container #stars span').text(barbershops[itemIndex].stars);
        for(var i =0; i< barbershops[itemIndex].haircut_types.length; i++){
            var haircut_type = $('<div class="bs-type">');
            var haircut_name = $('<h6>');
            haircut_name.text(barbershops[itemIndex].haircut_types[i].name);
            haircut_type.append(haircut_name);
            var haircut_price = $('<p class="price">');
            haircut_price.text(barbershops[itemIndex].haircut_types[i].price + 'Руб');
            haircut_type.append(haircut_price);
            var haircut_time = $('<p class="time">');
            haircut_time.text('60 мин');
            haircut_type.append(haircut_time);
        }
        $('#barber-info').fadeIn(300);
        setTimeout(function() {
            $('#main').fadeOut(100);
        },250);
        allSmallMarket();
        markerPom[itemIndex][0].setMap(null);
        markerPom[itemIndex][1].setMap(map);
    }

    $('#barber-info a#close').click(function() {
        $('#barber-info').fadeOut(300);
        setTimeout(function() {
            $('#main').fadeIn(100);
        },350);
    });

    $('.bs-type').click(function() {
        var vv = $(this).find('.price').find('span').html();
        var vv2 = $(this).find('h6').html();
        $('#booking-container form input[name="price"]').val(vv);
        $('#booking-container form input[name="bbName"]').val(vv2);
        $('#booking-container #booking-info .bb-price span').html(vv);
        $('#booking-container #booking-info .bb-info').html(vv2);
        $('#barber-choose-time').fadeIn(300);
        setTimeout(function() {
            $('#barber-info').fadeOut(100);
        },250);
        $('#date-slider').slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: false
        });

    });
    $('#barber-choose-time a#close').click(function() {
        $('#barber-choose-time').fadeOut(300);
        setTimeout(function() {
            $('#barber-info').fadeIn(100);
        },350);
    });

    $('#barber-choose-time-container #ok').click(function() {
        $('#booking').fadeIn(300);
        setTimeout(function() {
            $('#barber-choose-time').fadeOut(100);
        },250);
        $('#date-slider').slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: false
        });
    });
    $('#booking  a#close').click(function() {
        $('#booking').fadeOut(300);
        setTimeout(function() {
            $('#barber-choose-time').fadeIn(100);
        },350);
    });

    $('.time-item').click(function() {
        var vv = $(this).text();
        $('#booking-container form input[name="time"]').val(vv);
        $('#booking-container #booking-info .bb-date i').html(vv);
    });
    $('#date-slider .date-slide').click(function() {
        var vv = $(this).find('p').html();
        $('#booking-container form input[name="date"]').val(vv);
        $('#booking-container #booking-info .bb-date span').html(vv);
    });

    $('.time-item,#date-slider .date-slide').click(function() {
        if (($('#booking-container form input[name="time"]').val() != "") && ($('#booking-container form input[name="date"]').val() != "")) {
            $('#barber-choose-time-container #ok').removeClass('disable');
        }
    });

    $('#booking a#close').click(function() {
        $('#booking').fadeOut(300);
        setTimeout(function() {
            $('#barber-choose-time').fadeIn(100);
        },350);
    });
});

function initMap() {
	var mapCanvas = document.getElementById('map');
    var mapOptions = {
        center: {lat: 54.7330351, lng: 55.9536999},
        zoom: 15,
        panControl: false,
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        scrollwheel: false,
        overviewMapControl: false
    };

    map = new google.maps.Map(mapCanvas, mapOptions);

}

function Send() {

    var form = $('#booking-container form').serialize();
    $.ajax({
      type: "POST",
      url: "/api/barbershops/booking/add/",
      data: form,
      success: function() {
       alert('Бронь сделана')
      }
    });
};
