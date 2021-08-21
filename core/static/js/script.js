let burger = document.querySelector(".burger");
let burgerContent = document.querySelector(".burger__content");

burger.addEventListener("click", function () {
  console.log(burger);
  burger.classList.toggle("burger_active");
  burgerContent.classList.toggle("burger__content_active");
  console.log(burger);
});

function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Скрыть";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Читать Далее";
    moreText.style.display = "inline";
  }
}

$('.article__slider').slick({
  dots: false,
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  centerMode: true,
  variableWidth: true,
  autoplay: true,
  autoplaySpeed: 1500,
  pauseOnHover: false,
  focusOnSelect: true,
  slickPlay: true,
  arrows: false,
});

$('.news__boxes').slick({
  dots: false,
  infinite: true,
  speed: 200,
  slidesToShow: 1,
  centerMode: true,
  variableWidth: true,
  autoplay: true,
  autoplaySpeed: 1500,
  pauseOnHover: false,
  focusOnSelect: true,
  slickPlay: true,
  arrows: false,
});