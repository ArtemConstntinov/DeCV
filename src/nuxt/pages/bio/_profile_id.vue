<template>
	<v-container>

		<v-card class="info-card">
			<v-card-text class="profile-grid">
				<v-avatar
					color="grey"
					size="164"
				>
					<v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
				</v-avatar>

				<div class="bio-grid">
					<span class="headline">Jon Doe</span>
					<span>26</span>
					<span>Guangzhou</span>
				</div>
			</v-card-text>
		</v-card>


		<v-card
			class="info-card"
			v-for="(val, key) in validation_data"
			:key="key"
		>
			<v-card-text >
				<template v-if="Object.keys(val).length == 0">
					<v-alert

						type="warning"
						prominent
						border="left"
					>
						Information not found.
					</v-alert>
				</template>
				<template v-else v-for="(v, k) in val">
					<span class="subtitle-2 text-capitalize" :key="k + Date.now()">{{ k }}</span>:&nbsp;
					<span :key="k + Date.now()">{{ v }}</span><br :key="k + Date.now()">
				</template>
			</v-card-text>
		</v-card>

	</v-container>
</template>

<script lang="coffee">
export default {
	data: ->
		return {
			validation_data: {
				microsoft: {
					start_date: "23123",
					end_date: "a1345",
					position: "Developer"
					comments: ""
				},
				faceboock: {},
				google: {
					start_date: "3232",
					end_date: "422",
				}
			}
		}
}
</script>

<style lang="scss" scoped>
.info-card
{
	margin-bottom: 1rem;
}
.profile-grid
{
	display: grid;
	grid-template-columns: 164px repeat(4, minmax(1px, max-content));
	grid-gap: 2rem;
	.bio-grid
	{
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: repeat(auto-fit, minmax(1px, max-content));
		align-items: start;
	}
}

</style>