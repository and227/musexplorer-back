<template>
  <div>
    <ul :id="AlbumId" class="track"></ul>
  </div>
</template>

<script>
export default {
  props: ['AlbumId'],
  data() {
    return {
      tracksLink: 'https://musexplorer-test-01.herokuapp.com/api/tracks/',
      tracks: [],
      tracksUpdated: [],
      youtubeLinks: [],
      isActive: false,
    }
  },
  beforeUpdate() {
    this.tracks = []
    this.youtubeLinks = []

    axios
      .get(this.tracksLink + '?albums=' + this.AlbumId)
      .then((response) => {
        for (let i = 0; i < response.data.data.length; i++) {
          this.tracks.push(response.data.data[i].name)
          this.youtubeLinks.push(response.data.data[i].youtube_link)
        }
      })
      .then(() => {
        document.querySelector('.track').innerHTML = ''

        for (let i = 0; i < this.tracks.length; i++) {
          document.querySelector('#first').insertAdjacentText = 'Tracks'
          document
            .querySelector('.track')
            .insertAdjacentHTML(
              'beforeend',
              `<li><a style="font-size: 19px; font-family: 'Potta One', cursive; color: white; text-decoration: none;" href="${this.youtubeLinks[i]}">${this.tracks[i]}</a></li>`
            )
        }
      })
      .then(() => {
        document
          .querySelector('.track')
          .insertAdjacentHTML(
            'afterbegin',
            `<li style="font-family: 'Anton', sans-serif; font-size: 26px;" v-show="isActive" id="first">Tracks</li><hr v-show="isActive" />`
          )
        document
          .querySelector('.track')
          .insertAdjacentHTML('beforeend', `<hr v-show="isActive" />`)
        document.querySelector('.track').insertAdjacentHTML(
          'beforeend',
          `<li style="font-family: 'Anton', sans-serif;">
          All copyrights reserved
        </li>`
        )
      })
  },
}
</script>

<style scoped>
.track {
  display: grid;
  height: 400px;
  padding-left: 0;
  margin-bottom: 70px;
}
div {
  display: flex;
  justify-content: center;
}
ul {
  text-align: center;
}
ul li {
  width: max-content;
  text-align: center;
  margin: auto;
}
</style>
