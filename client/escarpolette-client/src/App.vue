<template>
	<div id="app">
		<v-app>
			<v-toolbar class="white--text" color="primary">
				<v-toolbar-title>Escarpolette</v-toolbar-title>
				<v-spacer></v-spacer>
				<v-toolbar-items class="hidden-sm-and-down">
					<v-btn flat>Reset la playlist</v-btn>
				</v-toolbar-items>
			</v-toolbar>
			<playlist></playlist>
			<item-form></item-form>
		</v-app>
	</div>
</template>

<script>
import Playlist from './components/Playlist.vue'
import ItemForm from './components/ItemForm.vue'

export default {
	name: 'app',
	components: {
		Playlist,
		ItemForm
	}
}
</script>

<style>
#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}
</style>
