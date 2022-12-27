<script>

	/**
	 * @type {number}
	 */
	let numerator = 0;
	/**
	 * @type {number}
	 */
	let denominator = 0;

	let response = ""
	async function divide() {
		const res = await fetch(`http://localhost:5000/python?num=${numerator}&den=${denominator}`);
		const [Q, R] = await res.json();
		
		response = `
		quotient: ${Q}\n
		rest: ${R}
		`
	}
</script>

<svelte:head>
	<title>Dividers Demos</title>
	<meta name="Demo" content="A demo for a backend division algorithm." />
</svelte:head>

<section>
	<h1>Dividers demo!</h1>

	<p>
		Hello there, this is my working demo on <a href="svelte.dev">Svelte</a>
		for a <a href="https://www.python.org/">python</a>
		<a href="https://flask.palletsprojects.com">flask</a> API
	</p>

	<h2>Python Algorithm</h2>
	<p>
		This uses the python algorithm to calculate the quotient and rest. If the numerator is positive,
		it calculates the division and then floors the result to calculate the quotient. Else, then
		calculates and ceil the result to get the quotient.
	</p>

	<div class="input-wrap">
		<label for="numerator">numerator: </label>
		<input type="number" name="numerator" id="numerator" bind:value={numerator}>
	</div>

	<div class="input-wrap">
		<label for="denominator">denominator: </label>
		<input type="number" name="denominator" id="denominator" bind:value={denominator}>	
	</div>

	<button on:click={divide}>Calculate!</button>
	<p>{response}</p>
</section>

<style>
	section {
		width: 50%;
		margin: auto;
	}
	.input-wrap {
		margin: 1em 0;
	}
</style>