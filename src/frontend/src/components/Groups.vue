<template>
  <ul>
    <li id="first">Groups</li>
    <hr />
    <li
      v-for="(group, index) in groupsAndAlbums"
      v-on:click="showConsole"
      v-bind:key="index"
      v-bind:id="group.album_uuid"
    >
      {{ group.album_group }}
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    groupsAndAlbums: Array,
  },
  data() {
    return {
      link: '',
      bandsAndAlbumsLink:
        'https://musexplorer-test-01.herokuapp.com/api/albums/',
      currentAlbum: '',
      currentId: '',
    }
  },
  methods: {
    showConsole(event) {
      this.link = event.target.id
      axios
        .get(this.bandsAndAlbumsLink + '?uuids=' + this.link)
        .then((response) => {
          this.currentAlbum = response.data.data[0].name
          this.currentId = response.data.data[0].album_uuid
          this.$emit('albumSave', this.currentAlbum)
          this.$emit('IdSave', this.currentId)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>

<style scoped>
ul {
  width: 300px;
  padding-left: 0;
}
ul li {
  font-family: 'East Sea Dokdo', cursive;
  font-size: 30px;
  cursor: pointer;
  width: max-content;
}
ul li:hover {
  opacity: 50%;
}
#first {
  font-family: 'Anton', sans-serif;
  font-size: 26px;
  opacity: 100%;
  cursor: default;
}
</style>
