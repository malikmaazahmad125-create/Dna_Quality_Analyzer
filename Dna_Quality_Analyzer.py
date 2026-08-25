import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("." * 30)

print("PROJECT : DNA QUALITY ANALYZER")

print("." * 30)


dna_sequence = "ATGCGATCGATCGATCGATGC"

dna_sequence = dna_sequence.upper().replace(" ", "")

print(dna_sequence)

print("\n", "." * 10, "DNA VALIDATION", "." * 10)


def valid_dna(sequence):

    valid_base = "ATGC"

    for base in sequence:

        if base not in valid_base:

            return False

    return True


result = valid_dna(dna_sequence)

print("Dna Sequence is:", result)


print("\n", "." * 10, "DNA LENGTH AND ITS COUNTS", "." * 10)

dna_length = len(dna_sequence)

print("Dna length is:", dna_length)

a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)


GC_CONTENT = (g_count + c_count) / dna_length * 100

print("GC_CONTENT is:", round(GC_CONTENT, 2), "%")


print("\n", "." * 10, "NUMPY STATISTICS", "." * 10)

numpy_counts = np.array([a_count, t_count, g_count, c_count])

print("dna_sequence_counts is:", numpy_counts)

print("\nStatistics methods:")

print("Maximum is:", np.max(numpy_counts))

print("Minimum is:", np.min(numpy_counts))

print("Average is:", np.mean(numpy_counts))


print("\n", "." * 10, "BOOLEAN FILTERING", "." * 10)

dna_counts = numpy_counts[numpy_counts > np.mean(numpy_counts)]

print("BOOLEAN FILTERING IS:", dna_counts)


print("\n", "." * 10, "DNA_SEQUENCE DATAFRAME", "." * 10)

dna_dataframe = pd.DataFrame({

    "dna": ["A", "T", "G", "C"],

    "Counts": [a_count, t_count, g_count, c_count]

})

print("dna_dataframe is:\n", dna_dataframe)


dna_dataframe["Count_Average"] = (
    dna_dataframe["Counts"] > np.mean(numpy_counts)
)

print(dna_dataframe)


print("\n", "." * 8, "CHECK_QUALITY_SCORE")

quality_score = 0

if 40 <= GC_CONTENT <= 60:

    quality_score = 100

elif 30 <= GC_CONTENT < 40 or 60 < GC_CONTENT <= 70:

    quality_score = 75

else:

    quality_score = 50


print("Quality_Score:", quality_score)


print("\n", "." * 10, "CHECK_QUALITY_LEVEL", "." * 10)

if quality_score == 100:

    quality_level = "Excellent"

elif quality_score == 75:

    quality_level = "Moderate"

else:

    quality_level = "Low"


print("Quality level is:", quality_level)


print("\n", "." * 8, "SUMMARY", "." * 8)

print("DNA SEQUENCE IS:", dna_sequence)

print("Sequence Length:", dna_length)

print("A Count:", a_count)

print("T Count:", t_count)

print("G Count:", g_count)

print("C Count:", c_count)

print("GC Content:", round(GC_CONTENT, 2), "%")

print("Quality Score:", quality_score)

print("Quality Level:", quality_level)


# ==================================================
# VISUALIZATION
# ==================================================

# Visualization 1: DNA Base Counts

plt.figure(figsize=(8, 5))

sns.barplot(
    x=["A", "T", "G", "C"],
    y=[a_count, t_count, g_count, c_count]
)

plt.title("DNA Base Counts")

plt.xlabel("DNA Base")

plt.ylabel("Count")

plt.tight_layout()

plt.show()


# Visualization 2: GC Content

plt.figure(figsize=(7, 5))

sns.barplot(
    x=["GC Content"],
    y=[GC_CONTENT]
)

plt.title("DNA GC Content")

plt.ylabel("Percentage")

plt.ylim(0, 100)

plt.tight_layout()

plt.show()


# Visualization 3: Quality Score

plt.figure(figsize=(7, 5))

sns.barplot(
    x=["Quality Score"],
    y=[quality_score]
)

plt.title("DNA Quality Score")

plt.ylabel("Score")

plt.ylim(0, 100)

plt.tight_layout()

plt.show()
