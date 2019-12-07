<template>
	<div id="app">
		<v-app>
			<v-content>
				<v-container fluid fill-height>
	        <v-layout align-center justify-center>
	          <v-flex xs12 sm8 md4>
							<v-toolbar class="white--text" color="primary">
								<v-toolbar-title>Escarpolette</v-toolbar-title>
								<v-spacer></v-spacer>
								<v-toolbar-items class="hidden-sm-and-down">
									<v-btn flat><v-icon size="40" color="white">account_circle</v-icon></v-btn>
								</v-toolbar-items>
							</v-toolbar>
							<playlist></playlist>
							<item-form></item-form>
						</v-flex>
					</v-layout>
				</v-container>
			</v-content>
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
}
</style>
