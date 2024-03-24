<script setup>
    import { ref } from "vue";

    const isHeaderOpen = ref(false);
</script>

<template>    
    <nav class="bg-transparent">
        <div class="w-screen flex flex-wrap items-center justify-between mx-auto h-auto">
            <div class="intro-l text-logo transition-all duration-500">
                <span class="header-text">CARSCAN</span>
            </div>
            <button @click="isHeaderOpen = !isHeaderOpen" type="button" style="border-radius: 50%; background-color: rgb(203 251 69);" class="intro-r transition-all duration-500 inline-flex items-center p-1 w-14 h-14 mr-6 mt-4 justify-center text-sm text-secondary focus:outline-none">
                <svg class="w-full h-full" version="1.1" id="hamburger_icon_Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 48 48" style="enable-background:new 0 0 48 48;" xml:space="preserve">                        
                    <defs>
                        <filter id="hamburger_icon_Adobe_OpacityMaskFilter" filterUnits="userSpaceOnUse" x="5.1" y="5.1" width="38.4" height="38.4">
                            <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0"></feColorMatrix>
                        </filter>
                    </defs>
                    <mask maskUnits="userSpaceOnUse" x="5.1" y="5.1" width="38.4" height="38.4" id="hamburger_icon_SVGID_1_">
                        <g class="hamburger_icon_st0">
                            <linearGradient id="hamburger_icon_SVGID_2_" gradientUnits="userSpaceOnUse" x1="-542.541" y1="791.7112" x2="-558.3387" y2="791.7112" gradientTransform="matrix(0.2803 -0.9599 0.9599 0.2803 -598.7552 -729.6553)">
                                <stop offset="0" style="stop-color:#000000"></stop>
                                <stop offset="1" style="stop-color:#FFFFFF"></stop>
                            </linearGradient>
                            <polygon class="hamburger_icon_st1" points="7.7,29.1 12.1,13.9 6.2,12.2 1.7,27.4"></polygon>
                            <linearGradient id="hamburger_icon_SVGID_3_" gradientUnits="userSpaceOnUse" x1="-617.0938" y1="116.5801" x2="-636.2781" y2="116.5801" gradientTransform="matrix(-0.8498 -0.5272 0.5272 -0.8498 -561.7367 -223.1417)">
                                <stop offset="0" style="stop-color:#000000"></stop>
                                <stop offset="1" style="stop-color:#FFFFFF"></stop>
                            </linearGradient>
                            <polygon class="hamburger_icon_st2" points="42,10.6 25.7,0.5 22.5,5.7 38.8,15.9"></polygon>
                            <rect x="0.1" y="30.5" class="hamburger_icon_st3" width="48" height="17.5"></rect>
                            <rect x="15.6" y="16.4" class="hamburger_icon_st3" width="32.3" height="22.1"></rect>
                            <rect x="-5.1" y="32.8" transform="matrix(0.2803 -0.9599 0.9599 0.2803 -32.4096 28.4982)" class="hamburger_icon_st3" width="15.8" height="6.2"></rect>
                            <rect x="45.6" y="8.4" transform="matrix(0.5272 -0.8498 0.8498 0.5272 7.7442 49.906)" class="hamburger_icon_st3" width="6.2" height="19.2"></rect>
                        </g>
                    </mask>
                    <path class="hamburger_icon_st4" d="M24.3,5.6c4.2,0,8.3,1.4,11.6,4c3.3,2.6,5.6,6.2,6.6,10.3c1,4.1,0.6,8.4-1.2,12.2c-1.7,3.8-4.7,6.9-8.4,8.9
                        c-3.7,1.9-8,2.5-12.1,1.8c-4.1-0.8-7.8-2.9-10.6-6.1c-2.7-3.2-4.4-7.2-4.6-11.3c-0.2-4.2,1-8.3,3.4-11.7" style="stroke: rgb(21, 21, 23);"></path>
                    <line class="hamburger_icon_st5" x1="18.4" y1="22.7" x2="29.6" y2="22.7" style="stroke: rgb(21, 21, 23);"></line>
                    <line class="hamburger_icon_st5" x1="18.4" y1="25.9" x2="29.6" y2="25.9" style="stroke: rgb(21, 21, 23);"></line>
                </svg>
            </button>
        </div>
    </nav>

    <Transition name="header">
        <div class="modal z-40" id="headerModal" v-if="isHeaderOpen">
            <div class="bg-accent h-full text-secondary p-6 absolute z-50 modal-content">
                <div class="h-full flex flex-col items-start justify-center px-12">
                    <a href="/" class="my-4">
                        <h2 class="text-4xl">
                            Home
                        </h2>
                    </a>
                    <a href="/about" class="my-4">
                        <h2 class="text-4xl">
                            About
                        </h2>
                    </a>
                    <a href="/contact" class="my-4">
                        <h2 class="text-4xl">
                            Contact
                        </h2>
                    </a>
                    <hr class="line-break my-10 w-2/3 mx-auto">
                    <span class="self-center text-xs font-light whitespace-nowrap capitalize">DESIGNED BY ANIRUDH R</span>
                </div>
                <div @click="isHeaderOpen = !isHeaderOpen" class="close p-2 cursor-pointer"></div>
            </div>
        </div>
    </Transition>
</template>

<style scoped>
    .header-enter-from {
        opacity: 0;
        display: none;
        transform: translateX(120%);
    }

    .header-enter-active, .header-leave-active {
        display: block;
        transition: all 0.5s ease-in-out;
    }

    .header-leave-to {
        opacity: 1;
        display: block;
        transform: translateX(120%);
    }

    .header-text {
        backface-visibility: hidden;
        will-change: transform;
        display: inline-block;
        translate: 0% 0%;
        stroke-dasharray: 1;
    }

    .text-logo {
        height: .7em;
        font-weight: 900;
        font-size: 12vw;
        line-height: .78;
        text-transform: uppercase;
        display: flex;
        overflow: hidden;
        text-wrap: nowrap;
        font-family: "wu";
        
    }

    @media (max-width: 1200px) {
        .text-logo {
            font-size:12.75vw
        }
    }

    @media (max-width: 1024px) {
        .text-logo {
            font-size:13.35vw
        }
    }

    @media (max-width: 768px) {
        .text-logo {
            font-size:14vw
        }
    }

    @media (max-width: 480px) {
        .text-logo {
            font-size:14.5vw
        }
    }

    .close {
        position: absolute;
        right: 30px;
        top: 30px;
        background-color: #151517;
        background-image: url(/svg/icon-close.svg);
        background-position: center;
        background-repeat: no-repeat;
        width: 48px;
        height: 48px;
        display: inline-block;
        border-radius: 100%;
        overflow: hidden;
    }

    .hamburger_icon_st0{filter:url(#hamburger_icon_Adobe_OpacityMaskFilter);}
    .hamburger_icon_st1{fill:url(#hamburger_icon_SVGID_2_);}
    .hamburger_icon_st2{fill:url(#hamburger_icon_SVGID_3_);}
    .hamburger_icon_st3{fill:#FFFFFF;}
    .hamburger_icon_st4{mask:url(#hamburger_icon_SVGID_1_);fill:none;stroke:#151517;}
    .hamburger_icon_st5{fill:none;stroke:#151517;}

    .modal-content {
        width: -webkit-fill-available;
    }

    .modal {
        position: fixed;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        overflow: hidden;
        padding-left: 17%;
    }

    .modal::before {
        background: rgba(0, 0, 0, 0.8);
        opacity: 0;
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        transition-duration: 700ms;
        transition-timing-function: ease-in-out;
        animation-duration: 700ms;
        animation-timing-function: ease-in-out;
        z-index: 1;
        transform: translate3d(0, 0, 0);
    }

    .line-break {
        border: none;
        height: 1px;
        background-color: #898990;
        opacity: 30%;
    }
</style>