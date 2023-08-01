<template>
  <!-- SECTION router-push to a page to purchase the video courses -->
  <section class="row">
    <div class="col-12 text-center ">
      <h1 class="text-dark text-uppercase">Learn from real top-1% etsy sellers</h1>
      <h4 class="text-secondary">No guesswork. No BW. Just proven strategies for success on Etsy</h4>
    </div>
  </section>
  <section class="row justify-content-center">
    <div class="col-12 col-md-4 text-center">

    </div>
  </section>
  <section class="row justify-content-center">
    <div class="col-12 col-md-7 mt-5 p-3">
      <h3 class="text-center">We Love Helping Other Etsy Sellers Succeed</h3>
      <p class="text-info text-center">Good advice can be hard to find:<br />We learned that the hard way.</p>
      <div class="text-max">
        <p>Our success on Etsy wasn't overnight. And it wasn't an accident, or "good luck."" It was the
          result of meticulous
          testing, research, mistakes (lots of mistakes) and doing more of what worked (and less of what didn't!). </p>
        <p>
          That's why, after years of hard work (and success in becoming a top-1% Etsy shop!) we love sending the elevator
          back down to other Etsy sellers who are in the same place we were at years ago. Because a rising tide lifts all
          ships. And when Etsy gets stronger as a platform with sellers who know the ropes, we all benefit.
        </p>
        <p>
          Our success is replicable. Which means that you can do it in your shop too. And we'd love to teach you how.
        </p>

      </div>

    </div>
    <div class="col-12 col-md-4 p-3 ">
      <img src="../assets/img/craftranker_main.jpg" class="img-fluid rounded img-height mt-5" />

    </div>
  </section>
  <hr />
  <section class="row">
    <div class="col-12">
      <h2 class="text-center">What Other Etsy Sellers Are Saying:</h2>
      <div class="card p-3 m-5 pos-rel bg-white">
        <img src="../assets/img/doubleQuote.png" class="quote-art" />
        <div>
          <p>My shop improved immediately.A highly recommended resource!</p>
          <h6>WoodenGiftCo</h6>

        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  setup() {
    return {}
  }
}
</script>

<style scoped lang="scss">
.text-max {
  margin: auto;
  max-width: 500px;
}


.img-height {
  max-height: 500px;
  width: 400px;
  object-fit: cover;
  object-position: center;
}

.pos-rel {
  position: relative;
}

.quote-art {
  height: 80px;
  position: absolute;
}
</style>
