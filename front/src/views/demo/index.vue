<template>
    <div>
        {{data}}
    </div>
</template>

<script>
import { demo } from '@/api/demo'


export default {
  data(){
      return {
          data: ""
      }
  },
  created() {
    this.getdemo()
  },
    methods: {
        getdemo(){
            demo().then(res=>{
            this.data = res
            console.log(this.data)
        });
        }
}
}
</script>
