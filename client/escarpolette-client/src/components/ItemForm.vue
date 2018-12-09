<template>
	<div>
		<input v-model="url">
		<v-btn color="primary" @click="sendUrl"> envoyer </v-btn>
	</div>

</template>
<script>
	import axios from 'axios'
	export default {
		data() {
			return {
				url: ""
			}
		},
		methods: {
			sendUrl(){
				axios.post(`http://192.168.1.28:5000/items`,{url: this.url}).then(response => {
					console.log(response)
				})
			}
		}
	}
</script>