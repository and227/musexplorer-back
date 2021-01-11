<template>
  <div id="app">
    <div id="windows">
      <Groups v-bind:groupsAndAlbums="groupsAndAlbums"></Groups>
      <Albums v-bind:groupsAndAlbums="groupsAndAlbums"></Albums>
    </div>
  </div>
</template>

<script>
import Albums from './components/Albums'
import Groups from './components/Groups'

export default {
  name: 'App',
  data() {
    return {
      info: null,
      isActive: true,
      groupsAndAlbums: [],
      bandsAndAlbumsLink:
        'https://musexplorer-test-01.herokuapp.com/api/albums/',
      tracksLink: 'https://musexplorer-test-01.herokuapp.com/api/tracks/',
    }
  },
  components: {
    Albums,
    Groups,
  },
  created() {
    axios
      .get(this.bandsAndAlbumsLink)
      .then((response) => {
        this.info = response
        this.groupsAndAlbums = response.data.data.data
      })
      .catch((error) => {
        console.log(error)
      })
    axios
      .get(
        this.bandsAndAlbumsLink +
          '?album_uuid=ff906365-91e1-43f3-9012-459a63689420'
      )
      .then((response) => {
        console.log(response)
      })
  },
  methods: {},
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#windows {
  display: flex;
  justify-content: space-evenly;
}
</style>
