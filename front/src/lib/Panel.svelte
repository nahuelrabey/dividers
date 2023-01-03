
<script lang="ts">
	// import Input from "$lib/NumberInput.svelte"
	export let onclick: ()=>void;
</script>

<div class="panel">
	<!-- <div class="input-wrap">
		<label for="numerator">numerator: </label>
		<input type="number" name="numerator" id="numerator" bind:value={numerator} />
	</div> -->
    <slot></slot>

	<button on:click={onclick}>Calculate!</button>
</div>

<style>
	.panel {
		margin: 2em 0;
	}
	.panel button {
		margin: auto;
		display: block;
		padding: 0.5em 2em;
		border: none;
		border-radius: 10px;
		background-color: rgb(250, 96, 30);
		color: white;
	}
	.panel button:hover {
		cursor: pointer;
		background-color: rgb(255, 132, 79);
		color: white;
	}
</style>