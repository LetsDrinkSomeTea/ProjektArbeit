-[ ] Internetquellen runterladen
  - Max (1-15); Julian (16-Ende)
-[ ] Videos erstellen 
- Entweder:
  - Grundlagen + Tacotron2 & Real-Time Voice Cloning
  - Grundlagen + DFL & DFLive

DFL
1. Video Deepfakes (2 Slide)
2. AutoEncoder (2 Slide)
3. GANs (2 Slide)
4. Praxis anwendung in DFL

```
2-5 Slides PowerPoint und dann 5-10 pro Tool
15-20min Video
```

### Video
1. Einführung in Video-Deepfakes
2. Anwendungsgebiete
3. Technologische Grundlage
   1. Autoencoder
   2. GANs
4. Ethisch
5. Workflows
   1. DFL
   2. DFLive

### Audio
1. Einführung in Audio-Deepfakes
2. Anwendungsgebiete
3. Technologische Grundlage
   1. TTS
   2. Real-Time Voice Cloning
4. Ethisch
5. Workflow
   1. Tacotron2
   2. Real-Time Voice Cloning

# Video

## 1. **Einführung in Video-Deepfakes**
- **Definition**: Video-Deepfakes sind synthetische audiovisuelle Inhalte, die mithilfe von KI und Deep Learning erstellt werden, um realistische Videos zu erzeugen, die Personen Handlungen ausführen oder Worte sagen lassen, die sie in Wirklichkeit nie getan haben.
- **Historie**: Erste Anwendungen entstanden in den 1990er Jahren, heute sind sie durch technische Fortschritte weit verbreitet und leicht zugänglich.

## 2. **Anwendungsgebiete**
- **Positive Anwendungsgebiete**: 
  - Filmindustrie (z.B. Schauspieler mit Stunt-Doubles ersetzen)
  - Bildung (historische Figuren zum Leben erwecken)
  - Marketing (virtuelle Anproben)
- **Negative Anwendungsgebiete**: 
  - Politische Manipulation (Falschaussagen von Politikern)
  - Erpressung (z.B. falsche Videos für Drohungen)
  - Verbreitung von Fake News

## 3. **Technologische Grundlagen**
   - **Autoencoder**:
     - **Funktionsweise**: Neuronale Netze, die Bilder in eine komprimierte Darstellung umwandeln und dann wieder rekonstruieren. Dabei lernen sie die wesentlichen Merkmale der Bilder, um sie später auf andere Gesichter anzuwenden.
     - **Anwendung**: Wird verwendet, um die Gesichter von zwei Personen zu tauschen, indem ein Bild der Zielperson encodiert und dann mit dem Decodierer der Quellperson rekonstruiert wird.

   - **GANs (Generative Adversarial Networks)**:
     - **Funktionsweise**: Besteht aus einem Generator und einem Diskriminator, die gegeneinander arbeiten, um realistische Bilder zu erzeugen. Der Generator erzeugt Bilder, die der Diskriminator bewertet, und so verbessert sich die Qualität stetig.
     - **Anwendung**: Weit verbreitet in der Erstellung von Deepfakes, da sie besonders realistische Gesichter erzeugen können.

## 4. **Ethische Überlegungen**
- **Risiken**: Täuschung, Verbreitung von Fehlinformationen, Identitätsdiebstahl, Rufschädigung.
- **Herausforderungen**: Schwierige Erkennung von Deepfakes, da die Technologie immer besser wird.
- **Maßnahmen**: Entwicklung von Erkennungstechnologien, gesetzliche Regelungen, Aufklärung der Öffentlichkeit.

## 5. **Workflows**
   - **DFL (DeepFaceLab)**:
     - **Schritt 1: Datensammlung**: Sammeln und Vorbereiten von Video- und Bildmaterial.
     - **Schritt 2: Preprocessing**: Gesichtsextraktion und Vorbereitung der Daten.
     - **Schritt 3: Modelltraining**: Trainieren eines Modells auf Basis der gesammelten Daten.
     - **Schritt 4: Face-Swapping**: Anwenden des trainierten Modells auf das Zielvideo.
     - **Schritt 5: Feinschliff**: Manuelles Bearbeiten von Artefakten für ein realistisches Ergebnis.

   - **DFLive (DeepFaceLive)**:
     - **Schritt 1: Datensammlung**: Vorbereitung von Live-Material.
     - **Schritt 2: Echtzeit-Gesichtserkennung**: Implementierung von Gesichtserkennungsalgorithmen für Live-Übertragungen.
     - **Schritt 3: Echtzeit-Deepfakes**: Anwenden des Modells in Echtzeit auf Video-Streams.
     - **Anwendung**: Videokonferenzen, Live-Streaming, Unterhaltung.


# Audio

## 1. **Einführung in Audio-Deepfakes**
- **Definition**: Audio-Deepfakes sind synthetische Audioaufnahmen, die durch KI generiert werden, um Stimmen zu imitieren oder gesprochene Inhalte zu manipulieren.
- **Technologische Entwicklung**: Fortschritte im Bereich Text-to-Speech und Voice Cloning ermöglichen realistische Stimmfälschungen.

## 2. **Anwendungsgebiete**
- **Positive Anwendungsgebiete**:
  - Barrierefreiheit (z.B. Text-to-Speech für sehbehinderte Personen)
  - Unterhaltung (z.B. Stimmen in Computerspielen oder Filmen)
- **Negative Anwendungsgebiete**:
  - Betrug (z.B. CEO-Fraud)
  - Identitätsdiebstahl (z.B. Stimmenklon für täuschende Telefonanrufe)
  - Manipulation in sozialen Medien

## 3. **Technologische Grundlagen**
   - **Text-to-Speech (TTS) - Tacotron2**:
     - **Funktionsweise**: Verwendet Sequenz-zu-Sequenz-Lernen, um Mel-Spektrogramme aus Text zu erzeugen. Diese werden dann in Sprachwellenformen umgewandelt.
     - **Merkmale**: Hohe Sprachqualität, Flexibilität, Integration mit Vocodern für noch realistischere Ergebnisse.

   - **Real-Time Voice Cloning**:
     - **Funktionsweise**: Klont eine Stimme in Echtzeit basierend auf einer kurzen Audioaufnahme.
     - **Merkmale**: Sofortige Anwendung in Echtzeitkommunikation, benötigt nur wenige Sekunden Audio als Ausgangsmaterial.

## 4. **Ethische Überlegungen**
- **Risiken**: Täuschung, Missbrauch in betrügerischen Aktivitäten, Verletzung der Privatsphäre.
- **Herausforderungen**: Schwierigkeit, gefälschte von echten Audioinhalten zu unterscheiden.
- **Maßnahmen**: Entwicklung von Erkennungstechnologien, rechtliche Regelungen, Sensibilisierung für die Bedrohungen.

## 5. **Workflows**
   - **Tacotron2**:
     - **Schritt 1: Datensammlung**: Aufnahmen von Sprachproben erstellen und als einzelne Dateien speichern.
     - **Schritt 2: Preprocessing**: Konvertierung der Audiodateien in das erforderliche Format und Erstellen von Transkripten.
     - **Schritt 3: Modelltraining**: Training von Tacotron2, um Mel-Spektrogramme aus Texteingaben zu erzeugen.
     - **Schritt 4: Audio-Synthese**: Umwandlung der Spektrogramme in Sprachwellenformen zur Erzeugung des finalen synthetischen Audios.

   - **Real-Time Voice Cloning**:
     - **Schritt 1: Aufnahme einer Kurzspur**: Erstellen einer kurzen Audioaufnahme der Zielstimme.
     - **Schritt 2: Extraktion von Merkmalen**: Analyse der Audioeigenschaften durch das Modell.
     - **Schritt 3: Echtzeit-Klonung**: Anwenden der geklonten Stimme auf neue Sprachinhalte in Echtzeit, z.B. durch Texteingabe oder Live-Audio.
