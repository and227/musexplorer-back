<template>
  <div id="app" class="hide">
    <div id="windows">
      <Groups
        v-on:albumSave="handleAlbum"
        v-on:IdSave="handleId"
        v-bind:groupsAndAlbums="groupsAndAlbums"
      ></Groups>
      <Albums
        v-bind:album="album"
        v-bind:id="id"
        v-bind:groupsAndAlbums="groupsAndAlbums"
        v-on:albumIdSave="handleAlbumId"
      ></Albums>
    </div>
    <Tracks v-bind:AlbumId="AlbumId"></Tracks>
  </div>
</template>

<script>
import Albums from './components/Albums'
import Groups from './components/Groups'
import Tracks from './components/Tracks'
// import Nav from './components/Nav'

export default {
  name: 'App',
  data() {
    return {
      info: null,
      isActive: true,
      groupsAndAlbums: [],
      album: '',
      id: '',
      AlbumId: '',
      bandsAndAlbumsLink:
        'https://musexplorer-test-01.herokuapp.com/api/albums/',
      tracksLink: 'https://musexplorer-test-01.herokuapp.com/api/tracks/',
    }
  },

  components: {
    Albums,
    Groups,
    Tracks,
  },

  created() {
    document.querySelector('#groups').addEventListener('click', this.getGroups)
  },

  methods: {
    getGroups() {
      document.querySelector('#app').classList.toggle('hide')
      axios
        .get(this.bandsAndAlbumsLink)
        .then((response) => {
          this.info = response
          this.groupsAndAlbums = response.data.data.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleAlbum(currentAlbum) {
      this.album = currentAlbum
    },
    handleId(currentId) {
      this.id = currentId
    },
    handleAlbumId(currentAlbumId) {
      this.AlbumId = currentAlbumId
    },
  },
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
