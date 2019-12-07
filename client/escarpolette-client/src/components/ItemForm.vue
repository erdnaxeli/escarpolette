<template>
	<div>
		<input >
		<form>
			<v-text-field
	              label="lien vers votre contenu"
	              v-model="url"
	            >
	        </v-text-field>
	        <v-btn color="secondary" @click="sendUrl"> envoyer </v-btn>
	    </form>
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
				}).catch(error => {
					console.log(error.response)
				})
			}
		}
	}
</script>