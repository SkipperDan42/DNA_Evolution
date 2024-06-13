import dna_dictionaries as dna

hairGenes = {"Hair Texture": dna.hair_textures,
             "Hair Type":    dna.hair_types,
             "Hair Colour":  dna.hair_colours}

eyeGenes = {"Eye Tone":      dna.eye_tones,
            "Eye Primary Colour":   dna.eye_primary_colours,
            "Eye Secondary Colour": dna.eye_secondary_colours}

skinGenes = {"Skin Type":   dna.skin_types,
             "Skin Tone":   dna.skin_tones,
             "Skin Colour": dna.skin_colours}

bodyGenes = {"Body Type":   dna.body_types,
             "Neck Type":   dna.neck_types,
             "Shoulder Type": dna.shoulder_types,
             "Chest Shape": dna.chest_shapes,
             "Waist Type": dna.waist_types,
             "Hip Type": dna.hip_types,
             "Heights":   dna.body_types}

facialGenes = {  "Facial Shape":   dna.facial_shapes,
                 "Forehead Shape":   dna.forehead_shapes,
                 "Eyebrow Shape": dna.eyebrow_shapes,
                 "Nose Shape": dna.nose_shapes,
                 "Cheeckbone Shape": dna.cheekbone_shapes,
                 "Chin Type": dna.chin_types}

bodyHairGenes = {"Hairline Type":   dna.hairline_types,
                 "Eyebrow Type":   dna.eyebrow_types,
                 "Eyelash Type": dna.eyelash_types,
                 "Body Hair Type": dna.body_hair_types}

eyeShapeGenes = {"Eye Shape":   dna.eye_shapes,
                 "Eyelid Shape":   dna.eyelid_shapes}

lipGenes = {"Smile Type":   dna.smile_types,
            "Lip Shape":   dna.lip_shapes}

teethGenes = {"Teeth Type":   dna.teeth_types}



allGenes = {
            "Skin": skinGenes,
            "Body": bodyGenes,
            "Hair": hairGenes,
            "Body Hair": bodyHairGenes,
            "Eyes":  eyeGenes,
            "Eye Shape": eyeShapeGenes,
            "Face": facialGenes,
            "Lips": lipGenes,
            "Teeth": teethGenes}