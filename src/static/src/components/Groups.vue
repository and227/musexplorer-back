<template>
  <ul>
    <li>Groups:</li>
    <hr />
    <li v-for="(group, index) in groupsAndAlbums" v-bind:key="index">
      {{ group.album_group }}
    </li>
  </ul>
</template>

<script>
export default {
  props: ['groupsAndAlbums'],
}
</script>

<style scoped>
ul {
  border: 2px solid black;
  width: 300px;
  padding-left: 0;
}
</style>
