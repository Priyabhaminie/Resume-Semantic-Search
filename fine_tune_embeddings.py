from sentence_transformers import SentenceTransformer, SentencesDataset, InputExample
from torch.utils.data import DataLoader
from sentence_transformers import losses

# Load dataset
train_examples = [InputExample(texts=['Resume text here'], label=0) for resume in resumes]
train_dataset = SentencesDataset(train_examples, model)
train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)

model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=100)
model.save('fine_tuned_model')
