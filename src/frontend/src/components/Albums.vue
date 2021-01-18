<template>
  <div>
    <ul>
      <li id="first">Albums</li>
      <hr />
      <li @click="showConsole" v-bind:id="id">
        {{ album }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['album', 'groupsAndAlbums', 'id'],
  data() {
    return {
      albumId: '',
    }
  },
  created() {},
  methods: {
    showConsole(event) {
      this.albumId = event.target.id
      this.$emit('albumIdSave', this.albumId)
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
  cursor: pointer;
  font-family: 'East Sea Dokdo', cursive;
  font-size: 36px;
  width: max-content;
}
#first {
  font-family: 'Anton', sans-serif;
  font-size: 26px;
  opacity: 100%;
  cursor: default;
}
ul li:hover {
  opacity: 50%;
}
</style>
