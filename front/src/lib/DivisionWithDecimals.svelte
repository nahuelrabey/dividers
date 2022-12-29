
<script lang="ts">
	import Input from "$lib/NumberInput.svelte"
	import Panel from "$lib/Panel.svelte"
	export let onclick: ()=>void;
	export let numerator: number 
	export let denominator: number
    export let steps: number
</script>

<Panel {onclick}>
	<Input name="numerator" bind:value={numerator}/>
	<Input name="denominator" bind:value={denominator}/>
    <Input name="steps" bind:value={steps}/>
</Panel>