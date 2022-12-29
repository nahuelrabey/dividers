<script lang="ts">
	import Katex from 'svelte-katex';
	import Panel from '$lib/DivisionWithDecimals.svelte';

	let numerator = 0;
	let denominator = 0;
	let steps = 0;
	let list: number[] = [];
	let error = '';
	async function divide() {
		if (denominator == 0) {
			error = "You can't divide by zero my friend";
			return;
		}

		error = '';

		const res = await fetch(
			`http://localhost:5000/python/withdecimals?num=${numerator}&den=${denominator}&steps=${steps}`
		);
		const json = await res.json()
		list = json.slice(1)
		console.log(list)
		console.log(res)
	}
</script>

<Panel bind:numerator bind:denominator bind:steps onclick={divide} />
<span class="alert">{error}</span>
<Katex displayMode>
	\frac{`{${numerator}}`}{`{${denominator}}`} = [{#each list as decimal} {decimal}, {/each}]
</Katex>

<style>
	.alert {
		text-align: center;
		color: red;
		display: block;
		margin: 1em 0;
	}
</style>
