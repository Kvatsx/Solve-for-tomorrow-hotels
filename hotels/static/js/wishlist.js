document.addEventListener('DOMContentLoaded', () => {

    $("#hotelList").empty();
    const request = new XMLHttpRequest();
    request.open('POST', '/getWishlist');
    request.onload = () => {
        console.log('onload');
        const data = JSON.parse(request.responseText);
        console.log(data)
        if (data.success) {
            data.hotels.forEach(addHotel);
        }
        else {
            document.querySelector('#hotelList').innerHTML = 'There was an error.';
        }
    }

    const data = new FormData();
    data.append('city_id', city_id);
    data.append('checkin', checkin);
    data.append('checkout', checkout);
    data.append('guestrooms', GuestRooms);
    data.append('next', localStorage.getItem('next'));

    request.send(data);

});


function addHotel(item, index) {
    const template = Handlebars.compile(document.querySelector('#hotel').innerHTML);
    const content = template({'hotel_name': item.hotel_name, 'location':item.location, 'image':item.image, 'score':item.score, 'reviewCount': item.reviewCount, 'ratingCount': item.ratingCount, "specialPrice": item.specialPrice, "id": index});
    document.querySelector('#hotelList').innerHTML += content;
};
