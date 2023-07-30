<template>
  <nav class="navbar navbar-expand-lg  bg-header px-5">
    <router-link class="navbar-brand d-flex" :to="{ name: 'Home' }">
      <div class="d-flex flex-column align-items-center">
        <img alt="logo" src="../assets/img/craftrankerLogo.png" height="200" />
      </div>
    </router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
      aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav me-auto">
        <li>
          <router-link :to="{ name: 'Home' }" class="btn lighten-30 selectable text-uppercase">
            Home
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'Home' }" class="btn lighten-30 selectable text-uppercase">
            Etsy Courses
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'Home' }" class="btn lighten-30 selectable text-uppercase">
            About Us
          </router-link>
        </li>
      </ul>
      <!-- LOGIN COMPONENT HERE -->
      <Login />
    </div>
  </nav>
</template>

<script>
import Login from './Login.vue';
export default {
  setup() {
    return {}
  },
  components: { Login }
}
</script>

<style scoped>
.bg-header {
  background-image: url('../assets/img/headerLongDarker.jpg');
  background-position: center;
  background-size: cover;
}

a:hover {
  text-decoration: none;
}

.nav-link {
  text-transform: uppercase;
}

nav {
  height: 200px;
}

/* .navbar-nav .router-link-exact-active {
  border-bottom: 2px solid var(--bs-dark);
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
} */

@media screen and (min-width: 768px) {
  nav {
    height: 400px;
  }
}
</style>
