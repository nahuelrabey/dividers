<script lang="ts">
	export let value: number 
	export let name: string 
</script>

<div>
	<label for="denominator">{name}: </label>
	<input type="number" name={name} id={name} bind:value={value} />
</div>

<style>
	div {
		width: 50%;
		margin: 1em auto;
		display: flex;
		justify-content: space-between;
	}
</style>