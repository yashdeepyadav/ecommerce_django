
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

        if (user == 'AnonymousUser'){
			console.log("User Not Logged In")
		}
		else{
        	console.log("user is authorized, adding")
     	    updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
  
	console.log('User is authenticated, adding item to cart...')
         
		var url = '/update_item/'
		if(productId && action == 'add'){
				fetch(url, {
					method:'POST',
					headers:{
						'Content-Type':'application/json',
						'X-CSRFToken':csrftoken,
					}, 
					body:JSON.stringify({'productId':productId, 'action':action})
				})
				.then((response) => {
				return response.json();
				})
				.then((data) => {
					console.log('data', data)
				});
		}
		else(productId && action== 'sub')
		{
				console.log("user is authorized, removing");
				// updateUserOrderRemove(productId, action)
		}
}


function updateUserOrderRemove(productId, action){
	console.log('User is authenticated, adding item to cart...')

		var url = '/update_item/'
        console.log("item removed")
}
