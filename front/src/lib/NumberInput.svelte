<script lang="ts">
	export let value: number 
	export let name: string 
	let width: number;
	$:ismob = width <= 600;
</script>

<svelte:window bind:innerWidth={width}/>

<div class={ismob? "mobile" : "desktop"}>
	<label for="denominator">{name}: </label>
	<input type="number" name={name} id={name} bind:value={value} />
</div>

<style>
	.mobile {
		width: 80%;
		margin: 1em auto;
	}
	.mobile input {
		width: 4em;
	}
	input {
		text-align: center;
	}
	div {
		width: 50%;
		margin: 1em auto;
		display: flex;
		justify-content: space-between;
	}
</style>