<template>
<v-app>

	<s-header/>

	<v-content>
		<transition name="view-animation" mode="out-in">
			<nuxt/>
		</transition>
	</v-content>



	<!-- <s-footer id="footer"/> -->

</v-app>
</template>

<script lang="coffee">
import Header from "~/components/Header"
# import Footer from "~/components/Footer"
# import Contacts from "~/components/Contacts"

export default {
	name: "base-layout"

	components: {
		"s-header": Header,
		# "s-footer": Footer,
		# "contacts": Contacts
	}
	data: ->
		return {
			clipped: false,
			drawer: false,
			menu: [
				{
					link: "/gallery/painting"
					name: "PAINTING"
				},
				{
					link: "/gallery/graphics"
					name: "GRAPHICS"
				},
				{
					link: "/gallery/hand-made"
					name: "HAND MADE"
				},
				{
					link: "/learn-about-art"
					name: "LEARN"
				},
				{
					link: "/news"
					name: "NEWS"
				},
				{
					link: "/bio"
					name: "BIO"
				},
				{
					action: -> $nuxt.$vuetify.goTo("#footer", $nuxt.options),
					name: "CONTACTS"
				},
			]
			items: [
				{ icon: 'apps', title: 'Welcome', to: '/' },
				{ icon: 'bubble_chart', title: 'Inspire', to: '/inspire' }
			],
			miniVariant: false,
			right: true,
			rightDrawer: false,
			duration: 300,
			offset: 0,
			easing: 'easeInOutCubic'
		}
	computed: {
		options: ->
			return {
				duration: this.duration,
				offset: this.offset,
				easing: this.easing
			}
	}

}
</script>


<style lang="scss">
$font-size-root: 14px !default;
$body-font-family: 'Hind Madurai', sans-serif !default;
html
{
	font-size: $font-size-root;
	.v-application
	{
		font-family: $body-font-family;
	}

}

.view-animation-enter-active, .view-animation-leave-active
{
	transition: all 0.4s cubic-bezier(0.550, 0.085, 0.680, 0.530) !important;
	transform:  perspective(20em) rotateX(0deg) scale(1) translateY(0em);
}

.view-animation-enter /* .list-leave-active below version 2.1.8 */
{
	opacity: 0;
	transform: perspective(20em) rotateX(-1deg) scale(0.9) translateY(3em);
}
.view-animation-leave-to /* .list-leave-active below version 2.1.8 */ {
	opacity: 0;
	transform: perspective(20em) rotateX(-1deg) scale(0.9) translateY(3em);
}

.home-link
{
	display: grid;
	align-items: center;
}
.v-carousel__controls
{
	background-color: transparent !important;
}
// .header-container
// {
// 	align-items: center;
// 	display: flex;
// 	flex: 1 1 100%;
// 	padding: 0 24px;
// 	margin: auto !important;
// 	width: 100%;
// 	height: 100%;
// }
.menu-btn
{
	color: #D1D3D4 !important;
}


.contacts-info
{

		padding: 1em;
		position: inherit;
		bottom: 2em;


}
</style>
