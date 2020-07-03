document.addEventListener('DOMContentLoaded', () => {
    localStorage.setItem('next', "null");

    document.querySelector("#search").onsubmit = () => {
        $("#hotelList").empty();
        const city = document.querySelector("#where");
        const city_id = city.options[city.selectedIndex].getAttribute("id");
        const checkin = document.querySelector("#checkIn").value;
        const checkout = document.querySelector("#checkOut").value;
        const GuestRooms = document.querySelector("#GuestRooms").value;
        console.log(city_id);
        console.log(checkin);
        console.log(checkout);
        console.log(GuestRooms);

        const request = new XMLHttpRequest();
        request.open('POST', '/getHotels');
        request.onload = () => {
            console.log('onload');
            const data = JSON.parse(request.responseText);
            console.log(data)
            if (data.success) {
                localStorage.setItem('next', data.data.next);
                data.data.hotels.forEach(addHotel);
                console.log(data.data.hotels);
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

        return false
    };
});


function addHotel(item, index) {
    const template = Handlebars.compile(document.querySelector('#hotel').innerHTML);
    const content = template({'hotel_name': item.hotel_name, 'location':item.location, 'image':item.image, 'score':item.score, 'reviewCount': item.reviewCount, 'ratingCount': item.ratingCount, "specialPrice": item.specialPrice, "id": index});
    document.querySelector('#hotelList').innerHTML += content;
};


function addWishlist(btn) {
    btn.classList.remove("bg-primary");
    btn.classList.add("bg-danger");
    btn.innerHTML = "Remove from Wishlist";

    var parent = btn.parentElement.parentElement;
    var kids = parent.childNodes;

    // const data = new FormData();
    // data.append('city_id', city_id);
    // data.append('checkin', checkin);
    // data.append('checkout', checkout);
    // data.append('guestrooms', GuestRooms);

    // const request = new XMLHttpRequest();
    // request.open('POST', '/getHotels');
    // request.onload = () => {
    //     console.log('onload');
    //     const data = JSON.parse(request.responseText);
    //     console.log(data)
    //     if (data.success) {
    //         localStorage.setItem('next', data.data.next);
    //         data.data.hotels.forEach(addHotel);
    //         console.log(data.data.hotels);
    //     }
    //     else {
    //         document.querySelector('#hotelList').innerHTML = 'There was an error.';
    //     }
    // }
    // request.send(data);

}