//Preloader
window.onload = function () {
    let prl = document.getElementById('preloader');
    prl.style.display = 'none';
    var tlHead = gsap.timeline();
    tlHead.from('.navigation .logo', {duration: 0.3, x: -100, opacity: 0});
    tlHead.from('.menu', {
        duration: 0.3,
        opacity: 0,
    });
    tlHead.from('.navigation .langs', {
        duration: 0.3,
        y: -30,
        opacity: 0,
    });
    tlHead.from('.navigation .contact-btn', {
        duration: 0.3,
        x: 50,
        opacity: 0,
    });
    tlHead.from('.navigation .cart', {
        duration: 0.3,
        x: 50,
        opacity: 0,
    });
};
//Preloader End

//All jQuery Codes
$(function () {
    $(window).on('scroll', function () {
        if (this.scrollY > 200) {
            $('.goTop').addClass('show');
            $('.navigation').addClass('sticky');
        } else {
            $('.goTop').removeClass('show');
            $('.navigation').removeClass('sticky');
        }
    });
    $('.mode_btn').click(function () {
        $(this).toggleClass('dark');
        $('body').toggleClass('dark');
    });
    $('.goTop').click(function () {
        scroll(0, 0);
    });
    $('.accordion_title').click(function () {
        $(this).parent().toggleClass('active').siblings().removeClass('active');
        $(this).parent().children('.accordion_content').slideToggle();
        $(this).parent().siblings().children('.accordion_content').slideUp();
    });
    $('.menu__item').mouseenter(function () {
        $(this)
            .children('.sub-menu')
            .addClass('show')
            .siblings()
            .removeClass('show');
    });
    $('.menu__item').mouseleave(function () {
        $(this).children('.sub-menu').removeClass('show');
    });
    $('.langs').mouseenter(function () {
        $(this).children('.other').addClass('show');
    });
    $('.langs').mouseleave(function () {
        $(this).children('.other').removeClass('show');
    });
    $('.video').click(function () {
        $(this).toggleClass('active');
    });
    $('.toggle-menu-btn').click(function () {
        $(this).toggleClass('active');
        $('.wrap').toggleClass('active');
    });
    var updateBtn = document.getElementsByClassName('update-btn')

    for (i = 0; i < updateBtn.length; i++) {
        console.log(this.dataset)
        updateBtn[i].addEventListener('click', function () {
            var productId = this.dataset.product
            var action = this.dataset.action
            if (user == 'AnonymousUser') {
                addCookieItem(productId, action)
            } else {
                updateUserOrder(productId, action)
                console.log("user is logged in")
            }
        })
    }
    
    function addCookieItem(productId, action) {
        console.log(cart[productId])
        if (action == "add") {
            if (cart[productId] == undefined) {
                cart[productId] = {"quantity": 1}
    
            } else {
                cart[productId]["quantity"] += 1
            }
        }
        if (action == "remove") {
            cart[productId]["quantity"] -= 1
    
            if (cart[productId]["quantity"] <= 0) {
                console.log("removing item")
                delete cart[productId]
            }
    
        }
        console.log("Cart: ", cart)
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        location.reload()
    }
    
    function updateUserOrder(product_id, action) {
        console.log(csrftoken)
    
        var url = '/update_item/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({'productId': product_id, "action": action})
        }).then((response) => {
            return response.json();
        }).then((data) => {
            console.log("Data: ", data)
            location.reload()
        })
    }

    $('.counter').counterUp({
        delay: 15,
        time: 2000,
    });
});
var viewportWidth = $(window).width();
if (viewportWidth <= 992) {
    $('.has-child').removeAttr('href');
}
//All jQuery Codes End

var controller = new ScrollMagic.Controller();

/*  Scroll Animations  */

var tl1 = gsap.timeline({paused: true});
tl1.from('.about__detail--title', {
    duration: 0.3,
    x: -50,
    opacity: 0,
});
tl1.from('.about__detail ul li', {
    duration: 0.3,
    x: -50,
    opacity: 0,
    stagger: 0.2,
});
var scroll1 = new ScrollMagic.Scene({
    triggerElement: '.about .section-title',
    triggerHook: 0.75,
})
    .setTween(tl1)
    // .addIndicators()
    .addTo(controller);
/////////////////////////////////////////////////////////////////
var tl2 = gsap.timeline({paused: true});
tl2.from('.products .owl-carousel', {
    duration: 0.3,
    y: 50,
    opacity: 0,
    stagger: 0.2,
});
var scroll2 = new ScrollMagic.Scene({
    triggerElement: '.products .section-title',
    triggerHook: 0.65,
})
    .setTween(tl2)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl3 = gsap.timeline({paused: true});
tl3.from('.features__item', {
    duration: 0.3,
    y: 50,
    opacity: 0,
    stagger: 0.25,
});
var scroll3 = new ScrollMagic.Scene({
    triggerElement: '.features .section-title',
    triggerHook: 0.65,
})
    .setTween(tl3)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl4 = gsap.timeline({paused: true});
tl4.from('.video', {
    duration: 0.3,
    x: -50,
    opacity: 0,
});
tl4.from('.video-guide .details .title', {
    duration: 0.3,
    x: 50,
    opacity: 0,
});
tl4.from('.video-guide .details .desc', {
    duration: 0.3,
    x: 50,
    opacity: 0,
    stagger: 0.25,
});
var scroll4 = new ScrollMagic.Scene({
    triggerElement: '.video-guide',
    triggerHook: 0.6,
})
    .setTween(tl4)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl5 = gsap.timeline({paused: true});
tl5.from('.details .tab-links li', {
    duration: 0.3,
    x: 50,
    scale: 0,
    opacity: 0,
    stagger: 0.25,
});
var scroll5 = new ScrollMagic.Scene({
    triggerElement: '.details .section-title',
    triggerHook: 0.65,
})
    .setTween(tl5)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl6 = gsap.timeline({paused: true});
tl6.from('.guides__item', {
    duration: 0.3,
    y: 50,
    opacity: 0,
    stagger: 0.25,
});
var scroll6 = new ScrollMagic.Scene({
    triggerElement: '.guides .section-title',
    triggerHook: 0.65,
})
    .setTween(tl6)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl7 = gsap.timeline({paused: true});
tl7.from('.answers img', {
    duration: 0.3,
    x: -50,
    opacity: 0,
});
tl7.from('.contact-block', {
    duration: 0.3,
    x: 50,
    opacity: 0,
});
var scroll7 = new ScrollMagic.Scene({
    triggerElement: '.answers',
    triggerHook: 0.65,
})
    .setTween(tl7)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////
var tl8 = gsap.timeline({paused: true});
tl8.from('.footer__top--menu', {
    duration: 0.3,
    y: 50,
    opacity: 0,
    stagger: 0.25,
});
tl8.from('.footer__top--info', {
    duration: 0.3,
    y: 50,
    opacity: 0,
});
tl8.from('.footer__main .app', {
    duration: 0.3,
    x: -50,
    opacity: 0,
});
tl8.from('.payments__item', {
    duration: 0.3,
    scale: 0,
    opacity: 0,
    stagger: 0.25,
});
var scroll8 = new ScrollMagic.Scene({
    triggerElement: '.footer',
    triggerHook: 0.8,
})
    .setTween(tl8)
    // .addIndicators()
    .addTo(controller);
//////////////////////////////////////////////////////////////

/*  Scroll Animations End  */

$('.slider .owl-carousel').owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    mouseDrag: false,
    autoplay: true,
    animateOut: 'slideOutUp',
    items: 1,
});

$('.products .owl-carousel').owlCarousel({
    loop: false,
    autoHeight: true,
    dots: false,
    nav: false,
    responsive: {
        0: {
            items: 1,
        },
        779: {
            items: 2,
        },
        1000: {
            items: 3,
        },
    },
});
$('.img-slider').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1,
        },
        1000: {
            items: 1,
        },
    },
});

$(function () {
    $('.tabs').tabs();
});
