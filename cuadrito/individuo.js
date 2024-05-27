import { readFileSync, writeFileSync } from "fs"
import { Genoma } from "./genoma.js"
import assert from "assert"

export class Individuo {
    /***
     * genoma := Genoma
     * fitness := int (sujeto a cambios)
    ***/
    constructor(genoma, fitness = 0) {
        this.genoma = genoma
        this.fitness = fitness
    }
    crossover(dominante, recesivo) {
        let offspring = new Genoma(dominante.genoma?.num_inputs, dominante.genoma?.num_outputs);
        let length_neuronas = dominante.genoma?.neuronas.length
        for (let i = 0; i < length_neuronas; i++) {
            let neurona_dom = dominante.genoma?.neuronas[i]
            let neuron_id = neurona_dom.neuron_id
            let neurona_rec = recesivo.genoma.find_neurona(neuron_id);
            if (neurona_rec == false) {
                offspring.add_neurona(neurona_dom)
            } else {
                offspring.add_neurona(neurona_dom.crossover(neurona_dom, neurona_rec))
            }
        }

        let length_links = dominante.genoma?.neuronas.length
        for (let i = 0; i < length_links; i++) {
            let enlace_dom = dominante.genoma?.links[i]
            let link_input_id = enlace_dom.input_id
            let link_output_id = enlace_dom.output_id
            let enlace_rec = recesivo.genoma.find_link(link_input_id, link_output_id)
            if (enlace_rec == false) {
                offspring.add_link(enlace_dom)
            } else {
                offspring.add_link(recesivo.crossover(enlace_dom, enlace_rec))
            }

        }
        return offspring
    }
}