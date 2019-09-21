<template>
	<div style="margin-bottom: 18rem;">
		<h2 class="display-1 text-center">Wanna check someone?</h2>
		<br>
		<v-card min-width="420">
			<v-form @submit.prevent="submit()">
				<div class="search-bar">
					<v-text-field
						label="Profile ID"
						solo
						hide-details
						flat
						v-model="profile_id"
					></v-text-field>
					<v-btn
						color="primary"
						depressed
						large
						height="48"
						:disabled="profile_id === '' || profile_id === null || loading"
						:loading="loading"
						type="submit"
					>
					Go
					</v-btn>
				</div>
			</v-form>
		</v-card>
	</div>
</template>

<script lang="coffee">
export default {
	layout: 'blank',
	data: -> return
		{
			profile_id: "",
			loading: false
		}

	methods:
		submit: ->
			unless @profile_id is '' or @profile_id is null
				@loading = true
				@$router.push({
					name: "bio-profile_id",
					params: { "profile_id": @profile_id }
				})

}
</script>

<style lang="scss" scoped>
.search-bar
{
	display: grid;
	grid-template-columns: 1fr auto
}
</style>

