var insta_thumb = document.getElementsByClassName('instagram-thumbnail');

for (var i = 0; i < insta_thumb.length; i++) {
	insta_thumb[i].onmousemove = function(){
		this.children[1].style.display = 'block';			
	}

	insta_thumb[i].onmouseout = function(){
		this.children[1].style.display = 'none';
	}
}