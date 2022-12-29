<script lang="ts">
	import Katex from 'svelte-katex';
	import Panel from '$lib/Division.svelte';

	let numerator = 0;
	let denominator = 0;
	let quotient = 0;
	let rest = 0;
	let error = '';
	async function divide() {
		if (denominator == 0) {
			error = "You can't divide by zero my friend";
			return;
		}

		error = '';

		const res = await fetch(`http://localhost:5000/python?num=${numerator}&den=${denominator}`);
		const [Q, R] = await res.json();

		quotient = Q;
		rest = R;
	}
</script>

<Panel bind:numerator bind:denominator onclick={divide}/>
<span class="alert">{error}</span>
<Katex displayMode>\frac{`{${numerator}}`}{`{${denominator}}`} = ({quotient}, {rest})</Katex>

<style>
	.alert {
		text-align: center;
		color: red;
		display: block;
		margin: 1em 0;
	}
</style>
