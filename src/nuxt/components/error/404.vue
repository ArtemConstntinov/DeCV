<template>
	<div class="error-404">
		<h1>This page doesn’t exist</h1>
		<p>The link you clicked on may be broken or no longer exist.</p>
	</div>
</template>
<script lang="coffee">
export default {
	name: 'error-404',
	props: {
		error: {
			type: Object,
			default: () => {}
		},
	},
}
</script>

<style lang="scss" scoped>
.error-404
{
	display: grid;
	height: calc(100vh - 62px);
	justify-content: center;
	align-content: center;
}
</style>
