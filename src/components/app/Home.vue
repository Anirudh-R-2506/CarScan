<script setup>
import { ref } from "vue";
import axios from "axios";
import { notify } from "notiwind"
import { ImgComparisonSlider } from '@img-comparison-slider/vue';

const isLoading = ref(false);
const image = ref(null);
const vehicleCount = ref(0);
const resultImage = ref("");
const inputImage = ref("");
const getBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
    });
};

function selectFiles() {
    image.value.click();  
}
async function imageSelected(event) {    
    isLoading.value = true;
    const img = await getBase64(event.target.files[0])
    console.log(img.split("data:image/jpeg;base64,")[1]);
    let formData = new FormData();
    formData.append("image", img.split("data:image/jpeg;base64,")[1])
    let response = await axios.post("http://127.0.0.1:5000/api/v1/count_vehicles", formData);
    console.log(response);
    if (response.data.status == 200){
        inputImage.value = img;
        resultImage.value = "data:image/jpeg;base64," + response.data.data.image;
        vehicleCount.value = response.data.data.count;
        isLoading.value = false;
        return;
    }
    notify({
        group: "error",
        title: "Error",
        text: "Unable to process image. Try again later!"
    }, 2000);
    isLoading.value = false;
}
</script>

<template>
    <Transition name="result">
        <div class="flex flex-col w-full h-full gap-2 p-6" v-if="resultImage.length == 0">
            <div class="flex flex-wrap items-center">                        
                <div class="flex flex-col items-start justify-between w-1/2 gap-1">
                    <span class="text-3xl font-thin duration-500 delay-500 intro-r text-accent">
                        Meet Carscan
                    </span>
                    <span class="text-2xl font-thin duration-500 delay-1000 intro-l">
                        Lightning-fast vehicle detection with unparalleled security
                    </span>            
                </div>            
                <div class="flex flex-col w-1/2 gap-3 -z-50">
                    <hr class="w-full h-5 duration-500 border-none opacity-100 bg-accent intro-l" style="transition-delay: 0ms;">
                    <hr class="w-full h-4 duration-500 border-none bg-accent opacity-80 intro-l1" style="transition-delay: 250ms;">
                    <hr class="w-full h-3 duration-500 border-none bg-accent opacity-60 intro-l2" style="transition-delay: 500ms;">
                    <hr class="w-full h-2 duration-500 border-none bg-accent opacity-40 intro-l3" style="transition-delay: 750ms;">
                    <hr class="w-full h-1 duration-500 border-none bg-accent opacity-20 intro-l4" style="transition-delay: 1000ms;">
                </div>
            </div>
            <div class="pl-6 w-full h-full border-accent border-solid border rounded-2xl flex items-center justify-center flex-col shadow-[0_3px_10px_rgb(255,255,255,0.2)]">            
                <div v-if="!isLoading" class="self-start rounded-full bg-accent w-7 h-7"></div>                                
                <div v-if="!isLoading" class="flex flex-col items-center justify-center text-sm duration-500 delay-1000 border border-solid rounded-full intro-l w-96 h-96 border-accent">
                    <input type="file" accept="" class="hidden" id="image" ref="image" @change="imageSelected">
                    <h1><span @click="selectFiles" class="underline cursor-pointer text-accent underline-offset-4">Choose</span> image to upload</h1>
                    <p class="text-tertiary">
                        Images uploaded will not be stored or misused in any form
                    </p>
                </div>
                <div v-else class="flex flex-col items-center justify-center duration-500 delay-1000 text-md intro-l">
                    <div role="status">
                        <svg aria-hidden="true" class="inline w-8 h-8 text-accent animate-spin fill-gray-300" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                            <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                        </svg>
                        <span class="sr-only">Loading...</span>                        
                    </div>
                    <p class="text-tertiary">
                        Beep beep! CarScan is crunching the numbers! Hang tight while we decode the traffic puzzle.
                    </p>
                </div>
            </div>
        </div>
    </Transition>     
    <Transition name="result">
        <div class="flex flex-col w-full h-full gap-2 p-6" v-if="resultImage.length > 0">
            <div class="flex flex-wrap items-center">
                <div class="flex items-center justify-between w-1/2">
                    <div class="flex flex-col items-start justify-between w-1/2 gap-1">
                        <span class="text-3xl font-thin duration-500 delay-500 intro-r text-accent">
                            Vehicles
                        </span>
                        <div class="transition-all duration-500 intro-l text-logo">
                            <span class="header-text">{{ vehicleCount }}</span>
                        </div>
                    </div>
                    <div class="flex items-end self-end justify-end w-1/2 gap-6 pr-4">
                        <div class="flex flex-col items-center justify-between gap-1">
                            <a :href="resultImage" download="result" target="_blank" style="border-radius: 50%; background-color: rgb(203 251 69);" class="inline-flex items-center justify-center p-1 text-sm transition-all duration-500 intro-r w-14 h-14 text-secondary focus:outline-none" aria-controls="navbar-default" aria-expanded="false">
                                <svg class="rotate-90" width="19" height="5" viewBox="0 0 19 5" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <line x1="10.915" y1="4.46484" x2="0.915039" y2="4.46484" stroke="#151517" style="stroke: rgb(21, 21, 23);"></line>
                                    <path d="M18.915 4.96484H13.7722H9.91504V0.964844L18.915 4.96484Z" fill="#151517" style="fill: rgb(21, 21, 23);"></path>
                                </svg>
                            </a>
                            <p class="text-sm text-tertiary">Download</p>
                        </div>
                        <div class="flex flex-col items-center justify-between gap-1">
                            <button @click="vehicleCount = 0; resultImage = '';" type="button" style="border-radius: 50%; background-color: rgb(203 251 69);" class="inline-flex items-center justify-center p-4 text-sm transition-all duration-500 intro-r w-14 h-14 text-secondary focus:outline-none" aria-controls="navbar-default" aria-expanded="false">                                
                                <svg viewBox="0 0 21 21" xmlns="http://www.w3.org/2000/svg" fill="#151517" stroke="#151517"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g fill="none" fill-rule="evenodd" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(0 1 1 0 2.5 2.5)"> <path d="m3.98652376 1.07807068c-2.38377179 1.38514556-3.98652376 3.96636605-3.98652376 6.92192932 0 4.418278 3.581722 8 8 8s8-3.581722 8-8-3.581722-8-8-8"></path> <path d="m4 1v4h-4" transform="matrix(1 0 0 -1 0 6)"></path> </g> </g></svg>
                            </button>
                            <p class="text-sm text-tertiary">Reset</p>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col w-1/2 gap-3 -z-50">
                    <hr class="w-full h-5 duration-500 border-none opacity-100 bg-accent intro-l" style="transition-delay: 5000ms;">
                    <hr class="w-full h-4 duration-500 border-none bg-accent opacity-80 intro-l1" style="transition-delay: 750ms;">
                    <hr class="w-full h-3 duration-500 border-none bg-accent opacity-60 intro-l2" style="transition-delay: 1000ms;">
                    <hr class="w-full h-2 duration-500 border-none bg-accent opacity-40 intro-l3" style="transition-delay: 1250ms;">
                    <hr class="w-full h-1 duration-500 border-none bg-accent opacity-20 intro-l4" style="transition-delay: 1500ms;">
                </div>
            </div>
            <div v-if="resultImage.length > 0" class="gap-3 w-full h-full border-accent border-solid border rounded-2xl flex items-center justify-center flex-col shadow-[0_3px_10px_rgb(255,255,255,0.2)]">
                <ImgComparisonSlider class="w-full outline-none rounded-2xl">
                    <img
                        slot="first"
                        style="width: 100%"
                        :src="inputImage"
                    />
                    <img
                        slot="second"
                        style="width: 100%"
                        :src="resultImage"
                    />
                </ImgComparisonSlider>
            </div>
        </div>
    </Transition>
</template>

<style scoped>
    .result-leave-to,
    .result-enter-from {
        opacity: 0;
    }
    .result-leave-from,
    .result-enter-to {
        opacity: 1;
    }
    .result-leave-active {
        opacity: 0;
        transition: all 0.5s ease;
    }
    .result-enter-active {
        transition: all 0.5s ease;
        opacity: 0;
    }
    .text-logo {
        height: auto;
        font-weight: 900;
        font-size: 8vw;
        line-height: .78;
        text-transform: uppercase;
        display: flex;
        overflow: hidden;
        text-wrap: nowrap;
        font-family: "wu";
        
    }
    .header-text {
        backface-visibility: hidden;
        will-change: transform;
        display: inline-block;
        translate: 0% 0%;
        stroke-dasharray: 1;
    }
</style>