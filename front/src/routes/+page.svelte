<script>
	import Katex from 'svelte-katex';

	/**
	 * @type {number}
	 */
	let numerator = 0;
	/**
	 * @type {number}
	 */
	let denominator = 0;

	let quotient = 0;
	let rest = 0;
	let error = '';
	async function divide() {
		if (denominator == 0){
			error = "You can't divide by zero my friend"
			return
		}

		error = ''

		const res = await fetch(`http://localhost:5000/python?num=${numerator}&den=${denominator}`);
		const [Q, R] = await res.json();

		quotient = Q;
		rest = R;
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
		Dividers API has a demonstration of the native division operator in python. We divide two
		numbers a/b, resulting in a float.
	</p>

	<p>
		If the result is larger than zero, later it will be rounded down (with the math.floor function)
		to the nearest integer; if it's less than zero, then it will be rounded up (with the math.ceil
		function) to the nearest integer.
	</p>

	<p>To get the rest we simply subtract from the numerator the quotient.</p>

	<div class="panel">
		<div class="input-wrap">
			<label for="numerator">numerator: </label>
			<input type="number" name="numerator" id="numerator" bind:value={numerator} />
		</div>

		<div class="input-wrap">
			<label for="denominator">denominator: </label>
			<input type="number" name="denominator" id="denominator" bind:value={denominator} />
		</div>

		<button on:click={divide}>Calculate!</button>
		
		<span class=alert>{error}</span>
	</div>

	<Katex displayMode>\frac{`{${numerator}}`}{`{${denominator}}`} = ({quotient}, {rest})</Katex>
</section>

<style>
	section {
		width: 50%;
		margin: auto;
	}

	h1,
	h2,
	p,
	span,
	label {
		font-family: sans-serif;
	}
	p {
		text-align: justify;
	}

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
	.input-wrap {
		width: 50%;
		margin: 1em auto;
		display: flex;
		justify-content: space-between;
	}

	.alert {
		text-align: center;
		color: red;
		display: block;
		margin: 1em 0;
	}
</style>
