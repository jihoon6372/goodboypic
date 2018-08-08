document.getElementById('header-menu-btn').onclick = function(){
	var menu = document.getElementById('mobile-header-menu');
	if (menu.className == 'menu-btn-row') {
		menu.className = 'menu-btn-row open'
	}else{
		menu.className = 'menu-btn-row'
	}
}