const toggle = document.querySelector('.toggle');
const closeBtn = document.querySelector('.close');
const showcase = document.querySelector('.showcase');
const menu = document.querySelector('.menu');

toggle.addEventListener('click', () => {
   toggle.classList.add('active');
   closeBtn.classList.add('active');
   showcase.classList.add('active');
   menu.classList.add('active');
});

closeBtn.addEventListener('click', () => {
   toggle.classList.remove('active');
   closeBtn.classList.remove('active');
   showcase.classList.remove('active');
   menu.classList.remove('active');
});
