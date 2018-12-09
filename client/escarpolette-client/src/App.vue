<template>
  <div id="app">
    <playlist></playlist>
    <item-form></item-form>
  </div>
</template>

<script>
import Playlist from './components/Playlist.vue'
import HelloWorld from './components/HelloWorld.vue'
import ItemForm from './components/ItemForm.vue'

export default {
  name: 'app',
  components: {
    Playlist,
    //'item-form': ItemForm
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
