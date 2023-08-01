<template>
  <header class="sticky-top">
    <Navbar />
  </header>
  <main>
    <router-view />
  </main>
  <footer>
    <section class="row justify-content-center">
      <div class="col-12 col-md-5 text-center pt-5">

        <img src="./assets/img/craftrankerLogo.png" height="120" />
      </div>

    </section>
    <section class="row justify-content-center">

      <div class="col-12 text-center">

        <h6 class="text-uppercase">
          <router-link :to="{ name: 'Home' }">
            <span>
              terms of service
            </span>
          </router-link> |
          <router-link :to="{ name: 'Home' }">
            <span>
              Privacy policy
            </span>
          </router-link>
        </h6>
      </div>
      <div class="col-6 col-md-4 text-center">
        <p>
          Disclaimer: Etsy is a trademark of Etsy, Inc.
          This content is not created or endorsed by Etsy, Inc.
          All Rights Reserved 2022 © Copyright CraftRanker
        </p>
      </div>
    </section>


  </footer>
</template>

<script>
import { computed } from 'vue'
import { AppState } from './AppState'
import Navbar from './components/Navbar.vue'

export default {
  setup() {
    return {
      appState: computed(() => AppState)
    }
  },
  components: { Navbar }
}
</script>
<style lang="scss">
@import "./assets/scss/main.scss";

:root {
  --main-height: calc(100vh - 32px - 64px);
}


footer {
  display: grid;
  place-content: center;

}
</style>
