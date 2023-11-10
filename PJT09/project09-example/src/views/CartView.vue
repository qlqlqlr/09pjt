<template>
    <div>
        <h1>장바구니</h1>
        <div v-if="cartItems">
        </div>
        <div v-else>
            <strong>장바구에 담긴 상품이 없습니다.</strong>
        </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { ref } from 'vue'

  const cartItems = ref([])
  const router = useRouter()

  cartItems.value = JSON.parse(localStorage.getItem('cart'))

//   const goDetail = (product) => {
//     router.push(`/${product.id}`)
//   }

  </script>
  
  <style scoped>
  
  </style>