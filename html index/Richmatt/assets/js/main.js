// Code for how it works sliding
let control = document.querySelectorAll('.control button')
let sliding = document.querySelectorAll('.sliding')
let slidingContainer = document.querySelector('.sliding-container')
let stepBox = $('.step-box')

function resizeSlider(){
	if (window.innerWidth <= '576'){
		slidingContainer.style.height = (stepBox.height() * 3.5)+'px'
	} else if (window.innerWidth <= '767'){
		slidingContainer.style.height = (stepBox.height() * 2.3)+'px'
	} else{
		slidingContainer.style.height = (stepBox.height() * 1.3)+'px'
	}
}
try{
	resizeSlider()
	$(window).resize(function(e){
		resizeSlider()
	})
} catch(e){
	
}



function clicked(e){
	let target = e.target
	control.forEach(i=>{
		if (i != target){
			i.classList.remove('active')
		}
	})
	target.classList.add('active')

	let boxid = target.getAttribute('box')
	sliding.forEach(i=>{
		if (i.id == boxid){
			i.classList.add('active')
			i.style.transform = 'translateX(0)'
			i.style.opacity = '1'
		} else {
			i.style.transform = 'translateX(100%)'
			i.style.opacity = '0'
			i.classList.remove('active')
			setTimeout(function () {
				i.style.transform = 'translateX(-100%)'
			}, 500)
			
		}
	})
}

control.forEach(i=>{
	i.addEventListener('click', clicked)
})


// Code for gallery box filter
let boxBtn = document.querySelectorAll('#gallery-nav .box li')
let galleryBox = document.querySelectorAll('.gallery-box')

function filtering(e){
	let target = e.target
	boxBtn.forEach(i=>{
		if (i != target){
			i.classList.remove('active')
		}
	})
	target.classList.add('active')

	let dataFilter = target.getAttribute('data-filter')
	if (dataFilter == 'all'){
		galleryBox.forEach(i=>{
			i.classList.add('active')
			i.classList.remove('deactivated')
		})
	} else {
		galleryBox.forEach(i=>{
			if (i.classList.contains(dataFilter)){
				i.classList.add('active')
				i.classList.remove('deactivated')
			} else {
				i.classList.remove('active')
				i.classList.add('deactivated')
			}
		})
	}
	
}

boxBtn.forEach(i=>{
	i.addEventListener('click', filtering)
})


// Code for popup images
$(".gallery-images").magnificPopup({
	delegate: ".gallery-box",
	type: "image",
	gallery: {
		enabled: true
	}
});