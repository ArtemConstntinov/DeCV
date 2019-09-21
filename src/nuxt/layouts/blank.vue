<template>
	<v-app>

		<v-content class="base-grid">
			<transition name="view-animation" mode="out-in">
				<nuxt />
			</transition>
		</v-content>

	</v-app>
</template>


<style lang="scss" scoped>
.base-grid
{
	display: grid;
	align-content: center;
	justify-content: center;
	background-color: #E6E7E8 !important;

	// &::after
	// {
	// 	content: "";
	// 	background-image: url('~static/svg/golden-aries.svg');
	// 	background-position: top right;
	// 	background-repeat: no-repeat;
	// 	opacity: 0.5;
	// 	top: 0;
	// 	left: 0;
	// 	bottom: 0;
	// 	right: 0;
	// 	position: absolute;
	// 	z-index: -1;
	// }
}

</style>
